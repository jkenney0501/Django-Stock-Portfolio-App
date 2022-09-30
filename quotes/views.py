from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

# Create your views here.
# everytime we create a web page, there needs to be a corresponding view
def home(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		
		api_request = requests.get("")

		# for error handling
		try:
			api = json.loads(api_request.content)
		#create an exception
		except Exception as e:
			api = "Sorry there is an error"
		return render(request, 'home.html', {'api': api} )
	else:
		return render(request, 'home.html', {'ticker': "Enter Ticker Symbol"} )

	

	#passes into home page
	#return render(request, 'home.html', {'api': api} )

def Page2(request):
	return render(request, 'Page2.html', {} )

def add_stock(request):
	import requests
	import json
	#lets us add tickers to the database to create a portfolio
	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock ticker has been added to your Portfolio!"))
			return redirect('add_stock')

	else:
		ticker = Stock.objects.all()
		output = []
		for ticker_item in ticker:
			api_request = requests.get("")

			# for error handling
			try:
				api = json.loads(api_request.content)
				output.append(api)
			#create an exception
			except Exception as e:
				api = "Sorry there is an error"
		return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock ticker has been removed from your Portfolio!"))
	return redirect(delete_stock)

def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker': ticker})
