from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request, 'pybo/main.html')

@login_required(login_url='common:login')
def marker(request):
    return render(request, 'pybo/marker.html')

@login_required(login_url='common:login')
def info(request):
    return render(request, 'pybo/info.html')

def gw(request):
    return render(request, 'pybo/gw.html')

def gb(request):
    return render(request, 'pybo/gb.html')

def gg(request):
    return render(request, 'pybo/gg.html')

def gj(request):
    return render(request, 'pybo/gj.html')

def dg(request):
    return render(request, 'pybo/dg.html')

def gn(request):
    return render(request, 'pybo/gn.html')

def us(request):
    return render(request, 'pybo/us.html')

def jn(request):
    return render(request, 'pybo/jn.html')

def jb(request):
    return render(request, 'pybo/jb.html')

def sj(request):
    return render(request, 'pybo/sj.html')

def so(request):
    return render(request, 'pybo/so.html')

def bs(request):
    return render(request, 'pybo/bs.html')

def jj(request):
    return render(request, 'pybo/jj.html')

def dj(request):
    return render(request, 'pybo/dj.html')

def ic(request):
    return render(request, 'pybo/ic.html')

def cb(request):
    return render(request, 'pybo/cb.html')

def cn(request):
    return render(request, 'pybo/cn.html')

@login_required(login_url='common:login')
def wcl(request):
    return render(request, 'pybo/wcl.html')

def wcl_gw(request):
    return render(request, 'pybo/wcl/gw.html')

def wcl_bs(request):
    return render(request, 'pybo/wcl/bs.html')

def wcl_cb(request):
    return render(request, 'pybo/wcl/cb.html')

def wcl_cn(request):
    return render(request, 'pybo/wcl/cn.html')

def wcl_dg(request):
    return render(request, 'pybo/wcl/dg.html')

def wcl_dj(request):
    return render(request, 'pybo/wcl/dj.html')

def wcl_gb(request):
    return render(request, 'pybo/wcl/gb.html')

def wcl_gn(request):
    return render(request, 'pybo/wcl/gn.html')

def wcl_gg(request):
    return render(request, 'pybo/wcl/gg.html')

def wcl_ic(request):
    return render(request, 'pybo/wcl/ic.html')

def wcl_jb(request):
    return render(request, 'pybo/wcl/jb.html')

def wcl_jn(request):
    return render(request, 'pybo/wcl/jn.html')

def wcl_jj(request):
    return render(request, 'pybo/wcl/jj.html')

def wcl_sj(request):
    return render(request, 'pybo/wcl/sj.html')

def wcl_so(request):
    return render(request, 'pybo/wcl/so.html')

def wcl_us(request):
    return render(request, 'pybo/wcl/us.html')

def wcl_gj(request):
    return render(request, 'pybo/wcl/gj.html')

@login_required(login_url='common:login')
def graph(request):
    return render(request, 'pybo/graph.html')

def graph1(request):
    return render(request, 'pybo/graph/2019_c.html')

def graph2(request):
    return render(request, 'pybo/graph/2020_c.html')

def graph3(request):
    return render(request, 'pybo/graph/2019_m.html')

def graph4(request):
    return render(request, 'pybo/graph/2020_m.html')