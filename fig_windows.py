import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["pdf.fonttype"]=42
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
x0=1700
rows=[("W1",1801,1802,1829,"fc"),("W2",1829,1830,1857,"fc"),("W3",1857,1858,1885,"fc"),
      ("Val.",1885,1886,1913,"val"),("W4 (test)",1913,1914,1941,"test")]
col={"train":"#b0b0b0","fc":"#9ecae1","val":"#e6e6e6","test":"#b22222"}
fig,ax=plt.subplots(figsize=(3.5,2.1))
for i,(n,te,s,e,k) in enumerate(rows):
    y=len(rows)-1-i
    ax.barh(y,te-x0+1,left=x0,height=0.55,color=col["train"])
    ax.barh(y,e-s+1,left=s,height=0.55,color=col[k],hatch="///" if k=="val" else None,
            edgecolor="#777" if k=="val" else col[k],linewidth=0.4)
ax.set_yticks(range(len(rows)))
ax.set_yticklabels([r[0] for r in rows][::-1],fontsize=7)
ax.set_xlim(x0,1945); ax.set_xlabel("Day index $d$ of the M5 calendar ($d_1$ = 29 Jan 2011)",fontsize=7)
ax.tick_params(axis="x",labelsize=7)
ax.set_xticks([1700,1800,1900,1941])
ax.text(x0+3,-0.9,"models use only the last 365 training days (grey, right part)",fontsize=5.5,color="#444")
ax.legend(handles=[Patch(color=col["train"],label="training data"),
   Patch(color=col["fc"],label="W1--W3: exploratory, excluded from article"),
   Patch(facecolor=col["val"],hatch="///",edgecolor="#777",label="validation (not used)"),
   Patch(color=col["test"],label="W4: scored test")],
   fontsize=6,loc="upper left",frameon=False,ncol=2,bbox_to_anchor=(0,1.30))
ax.set_ylim(-1.1,len(rows)-0.4)
for s in ("top","right"): ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig("fig_windows.pdf")
