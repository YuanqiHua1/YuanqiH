import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar

exp = np.load("I_q_IPA_exp.npy")
model = np.load("I_q_IPA_model.npy")

q_exp = exp[:, 0]
I_exp = exp[:, 1]

q_model = model[:, 0]
I_model = model[:, 1]

f = interp1d(q_model, I_model,  bounds_error=False, fill_value="extrapolate")
I_model_new = f(q_exp)

mask = np.isfinite(I_exp) & np.isfinite(I_model_new)
q_fit = q_exp[mask]
I_exp_fit = I_exp[mask]
I_model_fit = I_model_new[mask]

def error(scale):
    return np.sum((I_exp_fit - scale * I_model_fit)**2)

res = minimize_scalar(error)
scale = res.x

print("Best scale:", scale)

plt.figure()
plt.scatter(q_exp, I_exp, label="Experiment",color = 'red', alpha = 0.5, zorder = 3)
#plt.plot(q_model, I_model, label="Original_Model")
plt.plot(q_exp, scale * I_model_new, label="Opti_Model (scaled)", zorder = 2)


plt.legend()
plt.yscale('log')
plt.xlabel('q')
plt.ylabel('I(q)')
plt.show()
