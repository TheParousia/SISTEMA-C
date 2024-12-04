from django.shortcuts import render

# Create your views here.


def pagina_frete(request):

    if request.method == 'POST':
        peso = float(request.POST.get('peso'))
        distancia = float(request.POST.get('distancia'))
        tipo_entrega = request.POST.get('tipo_entrega')
        volume = float(request.POST.get('volume'))
        localidade = request.POST.get('localidade')
        valor_pedido = float(request.POST.get('valor_pedido'))

        valor_por_km = 0.5
        valor_frete = (peso / 1000) * distancia * valor_por_km

        if tipo_entrega == "expressa":
            valor_frete = valor_frete * +20
        elif tipo_entrega == "economica":
            valor_frete = valor_frete * -20

        if volume > 0.1:
            valor_frete += volume * 10

        if localidade == "rural":
            valor_frete = valor_frete + 5

        if valor_frete < 10:
            valor_frete = 100

        contexto = {
            'peso': peso,
            'distancia': distancia,
            'tipo_entrega': tipo_entrega,
            'volume': volume,
            'localidade': localidade,
            'valor_pedido': valor_pedido,
            'valor_frete': valor_frete,
        }

        return render(request, 'pagina_frete.html', contexto)

    return render(request, 'pagina_frete.html')
