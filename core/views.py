import os
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from groq import Groq

from .models import UserFinancialData
from .serializers import UserFinancialDataSerializer

# ---------- Frontend Template Views ----------

def index_view(request):
    return render(request, 'index.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def chat_view(request):
    return render(request, 'chat.html')

# ---------- API ENDPOINTS ----------

@api_view(['POST'])
def calculate_score(request):
    """
    Input: monthly_income, monthly_expenses, savings
    Logic: savings_rate = savings/income
    """
    data = request.data
    income = float(data.get('monthly_income') or 0)
    expenses = float(data.get('monthly_expenses') or 0)
    savings = float(data.get('savings') or 0)
    
    if income <= 0:
        return Response({'error': 'Income must be greater than zero.'}, status=400)
    
    # Save the data
    financial_data = UserFinancialData.objects.create(
        income=income,
        expenses=expenses,
        savings=savings
    )
    
    savings_rate = savings / income
    
    # Score out of 100
    if savings_rate >= 0.2:
        score = 85 + (savings_rate * 20) # e.g. 0.2 -> 89
    else:
        score = 40 + (savings_rate * 100) # e.g. 0.1 -> 50
        
    score = min(max(int(score), 0), 100) # Clamp between 0 and 100
    
    suggestions = []
    if savings_rate < 0.2:
        suggestions.append("Try to cut down discretionary expenses to reach the ideal 20% savings rule.")
        suggestions.append("Consider setting apart savings immediately when you receive your salary.")
    else:
        suggestions.append("Excellent saving habits! You have a healthy safety net.")
        suggestions.append("Consider investing your surplus savings for compounding returns.")
    
    return Response({
        'score': score,
        'savings_rate_percentage': round(savings_rate * 100, 1),
        'suggestions': suggestions
    })

@api_view(['POST'])
def suggest_sip(request):
    """
    Logic: disposable_income = income - expenses
    SIP = 30% of disposable_income
    """
    data = request.data
    income = float(data.get('monthly_income') or 0)
    expenses = float(data.get('monthly_expenses') or 0)
    
    disposable_income = income - expenses
    sip_amount = 0
    if disposable_income > 0:
        sip_amount = disposable_income * 0.30
        
    return Response({
        'disposable_income': disposable_income,
        'recommended_sip': round(sip_amount, 2),
        'explanation': "We recommend allocating 30% of your left-over disposable income directly into a Systematic Investment Plan (SIP) in mutual funds or index funds to beat inflation safely over time."
    })


@api_view(['POST'])
def ai_chat(request):
    """
    Calls Groq API with finance constraints.
    """
    message = request.data.get('message', '')
    if not message:
        return Response({'error': 'Message format missing'}, status=400)
        
    api_key = os.environ.get('GROQ_API_KEY')
    if not api_key:
        return Response({'error': 'Groq API key not configured on server. Did you set GROQ_API_KEY?'}, status=500)
        
    try:
        client = Groq(api_key=api_key)
        
        system_prompt = "Act as a friendly Indian financial advisor. Give simple, safe, beginner-level advice. Avoid risky or illegal suggestions. Keep responses concise."
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ]
        )
        
        return Response({
            'response': completion.choices[0].message.content
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)
