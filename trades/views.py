from django.shortcuts import render, get_object_or_404, redirect
from .models import Trade
from .forms import TradeForm

def trade_list(request):
    crypto_futures = Trade.objects.filter(trade_type='crypto_future')
    crypto_spot = Trade.objects.filter(trade_type='crypto_spot')
    forex = Trade.objects.filter(trade_type='forex')
    
    context = {
        'crypto_futures': crypto_futures,
        'crypto_spot': crypto_spot,
        'forex': forex,
    }
    
    return render(request, 'index.html', context)

def trade_detail(request, pk):
    trade = get_object_or_404(Trade, pk=pk)
    return render(request, 'trade_detail.html', {'trade': trade})

def add_trade(request):
    if request.method == "POST":
        form = TradeForm(request.POST, request.FILES)
        if form.is_valid():
            trade = form.save()
            return redirect('trade_detail', pk=trade.pk)
    else:
        form = TradeForm()
    return render(request, 'add_trade.html', {'form': form})

def edit_trade(request, pk):
    trade = get_object_or_404(Trade, pk=pk)
    if request.method == "POST":
        form = TradeForm(request.POST,  request.FILES, instance=trade)
        if form.is_valid():
            form.save()
            return redirect('trade_detail', pk=trade.pk)
    else:
        form = TradeForm(instance=trade)
    return render(request, 'trades/edit_trade.html', {'form': form})

def delete_trade(request, pk):
    trade = get_object_or_404(Trade, pk=pk)
    if request.method == "POST":
        trade.delete()
        return redirect('trade_list')
    return render(request, 'trades/confirm_delete.html', {'trade': trade})
