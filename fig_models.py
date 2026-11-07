import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["pdf.fonttype"]=42
import matplotlib.pyplot as plt
# real values from the pilot run (window W4, store CA_1, seed 0); Naive omitted for scale
m=["Seasonal naive","ETS","XGBoost (direct)","LightGBM (direct)","LightGBM (units$\\times$price)",
   "Hybrid (LGB+ETS)","LightGBM (hybrid rows)"]
w=[1.060,0.815,0.819,0.808,0.808,0.812,0.820]
r=[1271.2,1409.2,1494.3,1471.5,1410.3,1430.5,1473.6]
glob=[False,False,True,True,True,True,True]
fig,axs=plt.subplots(1,2,figsize=(3.5,2.3),sharey=True)
y=list(range(len(m)))[::-1]
for ax,v,xl,fmt,lim in ((axs[0],w,"WRMSSE (unitless)","{:.3f}",(0.74,1.18)),
                        (axs[1],r,"RMSE (USD/day)","{:.0f}",(1150,1750))):
    for yi,vi,g in zip(y,v,glob):
        ax.plot(vi,yi,"o" if g else "s",color="#1f4e79" if g else "#b22222",ms=3.5)
        ax.text(vi,yi+0.28,fmt.format(vi),fontsize=5,ha="center")
    ax.set_xlim(*lim); ax.set_xlabel(xl,fontsize=6.5); ax.tick_params(labelsize=6)
    ax.grid(axis="x",lw=0.3,color="#ccc")
    for s in ("top","right"): ax.spines[s].set_visible(False)
axs[0].set_yticks(y); axs[0].set_yticklabels(m,fontsize=6)
axs[0].set_ylim(-0.6,len(m)-0.3)
fig.tight_layout(w_pad=0.6)
fig.savefig("fig_models.pdf")
