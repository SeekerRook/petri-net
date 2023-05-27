import petri_net as pn

description =dict(
        t1=pn.Transition(
            [pn.Out(pn.ps[0])], 
            [pn.In(pn.ps[1]), pn.In(ps[2])]
            ),
        t2=pn.Transition(
            [pn.Out(pn.ps[1]), pn.Out(pn.ps[2])], 
            [pn.In(pn.ps[3]), pn.In(pn.ps[0])]
            ),
        )