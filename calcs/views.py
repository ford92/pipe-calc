from django.shortcuts import render
import math
from .function import pipecalc, linercalc
from .models import Pipe, Liner
from .forms import NameForm, LinerForm
# Create your views here.

def index(request):
	"""The home page for calcs."""
	return render(request, 'calcs/index.html')

def pipeflow(request):

	output_1 = 0
	output_2 = 0
	if request.method != 'POST':
		form = NameForm()

	elif request.method == 'POST' and 'submitform' in request.POST:
		form = NameForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			input1 = cd['ex_diameter']
			input2 = cd['ex_construction']
			input3 = float(cd['ex_length'])
			input4 = float(cd['ex_inlet'])
			input5 = float(cd['ex_outlet'])

			input6 = cd['pro_diameter']
			input7 = cd['pro_construction']
			input8 = float(cd['pro_length'])
			input9 = float(cd['pro_inlet'])
			input10 = float(cd['pro_outlet'])
		
			pipecalc(input1, input2, input3, input4, input5)
			output_1 = pipecalc.Q


			pipecalc(input6, input7, input8, input9, input10)
			output_2 = pipecalc.Q
	

	context = {
		'form': form,
		'output_1':output_1,
		'output_2':output_2,
	}
			

	return render(request, 'calcs/pipeflow.html', context)


def uvsize(request):
	"""The home page for calcs."""
	output_1 = 0
	output_2 = 0
	output_3 = 0
	output_4 = 0
	if request.method != 'POST':
		form = LinerForm()

	elif request.method == 'POST':
		form = LinerForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			input1 = cd['diameter']
			input2 = cd['shape']
			input3 = cd['distance']
		
			linercalc(input1, input2, input3)
			output_1 = linercalc.doc
			output_2 = linercalc.thickness
			output_3 = linercalc.external
			output_4 = linercalc.internal


	context = {
		'form': form,
		'output_1':output_1,
		'output_2':output_2,
		'output_3':output_3,
		'output_4':output_4,
	}

	return render(request, 'calcs/uvsize.html', context)
