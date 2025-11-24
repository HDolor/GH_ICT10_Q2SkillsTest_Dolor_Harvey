from pyscript import display, document
def clu(b):
    clu=document.getElementById('c').value
    document.getElementById('out').innerHTML=" "
    clu=str(clu)
    s="sci"
    m="mat"
    c="com"
    en="Science Club\n"
    ce={'Description':'Club for all Science interested students',
        'Meeting Time':'2pm',
        'Location':'Room 712',
        'Coordinator':'Sir Celzo',
        'Number of Members':'12',
        'Category':'Academic',
}
    he="Math Club"
    ma={'Description':'Club for smart Mathematician students',
        'Meeting Time':'2pm',
        'Location':'Room 712',
        'Coordinator':'Sir Tamon',
        'Number of Members':'12',
        'Category':'Academic',
}
    mu="Communcation Arts Club"
    ni={'Description':'Club for students to be more open',
        'Meeting Time':'2pm',
        'Location':'Room 711',
        'Coordinator':'Sir Thurnman',
        'Number of Members':'12',
        'Category':'Academic',
}
    if((clu==s)==True):
        clu=str(ce)
        clu=clu.replace("{"," ")
        clu=clu.replace("}"," ")
        clu=clu.replace("'"," ")
        display(f'{en}\n {clu}', target='out')
    if((clu==m)==True):
        clu=str(ma)
        clu=clu.replace("{"," ")
        clu=clu.replace("}"," ")
        clu=clu.replace("'"," ")
        display(f'{he}\n {clu}', target='out')
    if((clu==c)==True):
        clu=str(ni)
        clu=clu.replace("{"," ")
        clu=clu.replace("}"," ")
        clu=clu.replace("'"," ")
        display(f'{mu}\n {clu}', target='out')