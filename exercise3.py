import numpy as np
import scipy.stats

# This is how we import the module of Matplotlib we'll use later
import matplotlib.pyplot as plt

import seaborn as sns

def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """
    Compute the fold change
    """
    temp1 = (1 + c / KdA)**2
    temp2 = (1 + c / KdI)**2
    v_up = RK * temp1
    v_down = temp1 + Kswitch * temp2
    return (1+ v_up / v_down)**-1





rc={'lines.linewidth' : 2, 'axes.labelsize' : 18, 'axes.titlesize' : 18}
sns.set(rc=rc)

wt_lac = np.loadtxt('data/wt_lac.csv', delimiter = ',', skiprows = 3)
q18a_lac = np.loadtxt('data/q18a_lac.csv', delimiter = ',', skiprows = 3)
q18m_lac = np.loadtxt('data/q18m_lac.csv', delimiter = ',', skiprows = 3)

# Slice out iptg and fold change
wt_iptg = wt_lac[:,0]
wt_fc = wt_lac[:,1]
q18a_iptg = q18a_lac[:,0]
q18a_fc = q18a_lac[:,1]
q18m_iptg = q18m_lac[:,0]
q18m_fc = q18m_lac[:,1]

# Plot iptg - fold change
plt.close()
plt.semilogx(wt_iptg, wt_fc, linestyle='none', marker='.', markersize=20)
plt.semilogx(q18a_iptg, q18a_fc, linestyle='none', marker='.', markersize=20)
plt.semilogx(q18m_iptg, q18m_fc, linestyle='none', marker='.', markersize=20)
plt.xlabel('IPTG (mM)')
plt.ylabel('Fold Change')
plt.title('IPTG - Fold Change')


# Plot
x_wt = np.logspace(-5, 1)
y_wt = fold_change(x_wt, 141.5)
x_q18a = np.logspace(-5, 1)
y_q18a = fold_change(x_q18a, 16.56)
x_q18m = np.logspace(-5, 1)
y_q18m = fold_change(x_q18m, 1332)

plt.plot(x_wt, y_wt, linestyle='none', marker='.', markersize=20)
plt.plot(x_q18a, y_q18a, linestyle='none', marker='.', markersize=20)
plt.plot(x_q18m, y_q18m, linestyle='none', marker='.', markersize=20)

plt.legend(('wt_ex', 'q18a_ex', 'q18m_ex', 'wt_ca', 'q18a_ca', 'q18m_ca'), loc = 'lower right')

plt.show()
