from django.http import JsonResponse


# Create your views here.
from cep.models import Cep


def api_cep(request, cep):
    achar = Cep.objects.get(cep=cep)
    dados = {"rua": achar.rua, "bairro": achar.bairro, "cidade": achar.cidade, "estado": achar.estado, "complemento": achar.complemento}
    return JsonResponse(dados)
