import matplotlib.pyplot as plt

# Initial time
t0 = 0
# Final time
tf = 1
# Time step size
step = 0.01

# Transmission rate due to contacts with susceptible subject and an infected
alpha = 0.57;
# Transmission rate due to contacts with diagnosed
beta = 0.0114;
# Transmission rate due to contacts with ailing
gamma = 0.456;
# Transmission rate due to contacts with recognized subject
delta = 0.0114;
# Detection rate for ASYMPTOMATIC
epsilon = 0.171;
# Detection rate for SYMPTOMATIC
theta = 0.3705;
# Worsening rate: UNDETECTED asymptomatic infected becomes symptomatic
zeta = 0.1254;
# Worsening rate: DETECTED asymptomatic infected becomes symptomatic
eta = 0.1254;
# Worsening rate: UNDETECTED symptomatic infected develop life-threatening
mu = 0.0171;
# Worsening rate: DETECTED symptomatic infected develop life-threatening
nu = 0.0274;
# Mortality rate for infected with life-threatening symptoms
tau = 0.01;
# Recovery rate for undetected asymptomatic infected
lmbda = 0.0342;
# Recovery rate for detected asymptomatic infected
rho = 0.0342;
# Recovery rate for undetected symptomatic infected
kappa = 0.0171;
# Recovery rate for detected symptomatic infected
xi = 0.0171;
# Recovery rate for life-threatened symptomatic infected
sigma = 0.0171;


# ODE functions
def dot_S(S, I, D, A, R):
    return -1*S*(alpha*I + beta*D + gamma*A + delta*R)

def dot_I(S, I, D, A, R):
    return S*(alpha*I + beta*D + gamma*A + delta*R) - (epsilon+zeta+lmbda)*I

def dot_D(I, D):
    return epsilon*I - (eta + rho)*D

def dot_A(I, A):
    return zeta*I - (theta + mu + kappa)*A

def dot_R(D, A, R):
    return eta*D + theta*A - (nu + xi)*R



# Initial condition
# Population size
population = 50000000
# Infected
I = [200/population]
# Diagnosed
D = [20/population]
# Ailing
A = [1/population]
# Recognized
R = [2/population]
# Threatened
T = [0.00]
# Healed
H = [0.00]
# Extinct
E = [0.00]
# Susceptible
S = [1-I[0]-D[0]-A[0]-R[0]-T[0]-H[0]-E[0]]

number_of_steps = int((tf-t0)/step)
for t in range(1, number_of_steps + 1):
    prev = t-1
    # Update all variables
    S.append(S[prev] + dot_S(S[prev], I[prev], D[prev], A[prev], R[prev]))
    I.append(I[prev] + dot_I(S[prev], I[prev], D[prev], A[prev], R[prev]))
    D.append(D[prev] + dot_D(I[prev], D[prev]))
    A.append(A[prev] + dot_A(I[prev], A[prev]))
    R.append(R[prev] + dot_R(D[prev], A[prev], R[prev]))

    
## Plot the result
plt.plot(S, 'b-', label='Susceptible', linewidth=.5)
plt.plot(I, 'g-', label='Infected', linewidth=.5)
plt.plot(D, 'r-', label='Diagnosed', linewidth=.5)
plt.plot(A, 'c-', label='Ailing', linewidth=.5)
plt.plot(R, 'm-', label='Recognized', linewidth=.5)

plt.xlabel('Time (days)')
plt.ylabel('Population (people)')
plt.legend(loc="upper right")
plt.gcf().set_dpi(160)
plt.show()
