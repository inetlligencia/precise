from precise.skaters.managers.schurmanagerfactory import schur_weak_weak_pm_manager_factory, \
    schur_weak_weak_ewa_manager_factory, schur_vol_vol_ewa_manager_factory, schur_weak_vol_ewa_manager_factory


# Some additional Hierarchical Risk-Parity managers that seem to do okay
# (i.e. Schur managers with gamma=delta=0,j=j,q=q)


def hrp_weak_weak_pm_t0_d0_r025_n50_s5_long_manager(y, s, k=1, e=1,j=1,q=1.0):
    assert k==1
    return schur_weak_weak_pm_manager_factory(y=y, s=s, target=0, r=0.025, n_emp=50, n_split=5, e=e, gamma=0, delta=0,j=j,q=q)


def hrp_vol_vol_pm_t0_d0_r025_n50_s5_long_manager(y, s, k=1, e=1,j=1,q=1.0):
    assert k==1
    return schur_vol_vol_ewa_manager_factory(y=y, s=s, r=0.025, n_emp=50, n_split=5, e=e, gamma=0, delta=0,j=j,q=q)


def hrp_vol_vol_pm_t0_d0_r025_n50_s50_long_manager(y, s, k=1, e=1,j=1,q=1.0):
    assert k==1
    return schur_vol_vol_ewa_manager_factory(y=y, s=s, r=0.025, n_emp=50, n_split=50, e=e, gamma=0, delta=0,j=j,q=q)


def hrp_weak_vol_ewa_r025_n50_s50_long_manager(y, s, k=1, e=1,j=1,q=1.0):
    assert k==1
    return schur_weak_vol_ewa_manager_factory(y=y, s=s, r=0.025, n_emp=50, n_split=50, e=e, gamma=0, delta=0,j=j,q=q)


def hrp_weak_vol_ewa_r025_n50_s50_l10_long_manager(y, s, k=1, e=1,j=1,q=1.0):
    assert k==1
    return schur_weak_vol_ewa_manager_factory(y=y, s=s, r=0.025, n_emp=50, n_split=50, e=e, gamma=0, delta=0,j=j,q=q,l=10)


def hrp_weak_vol_ewa_r001_n200_s50_l20_long_manager(y, s, k=1, e=1,j=1,q=1.0):
    assert k==1
    return schur_weak_vol_ewa_manager_factory(y=y, s=s, r=0.001, n_emp=200, n_split=50, e=e, gamma=0, delta=0,j=j,q=q,l=20)


def hrp_weak_vol_ewa_r001_n200_s50_l100_long_manager(y, s, k=1, e=1,j=1,q=1.0):
    assert k==1
    return schur_weak_vol_ewa_manager_factory(y=y, s=s, r=0.001, n_emp=200, n_split=50, e=e, gamma=0, delta=0,j=j,q=q,l=100)


def hrp_weak_vol_ewa_r001_n200_s50_l21_long_manager(y, s, k=1, e=1,j=1,q=1.0):
    assert k==1
    return schur_weak_vol_ewa_manager_factory(y=y, s=s, r=0.001, n_emp=200, n_split=50, e=e, gamma=0, delta=0,j=j,q=q,l=21)


def hrp_weak_vol_ewa_r001_n200_s50_g050_l21_long_manager(y, s, k=1, e=1,j=1,q=1.0):
    assert k==1
    return schur_weak_vol_ewa_manager_factory(y=y, s=s, r=0.001, n_emp=200, n_split=50, e=e, gamma=0.5, delta=0,j=j,q=q,l=21)



HRP_LONG_MANAGERS = [ hrp_weak_weak_pm_t0_d0_r025_n50_s5_long_manager,
                      hrp_vol_vol_pm_t0_d0_r025_n50_s5_long_manager,
                      hrp_vol_vol_pm_t0_d0_r025_n50_s50_long_manager,
                      hrp_weak_vol_ewa_r025_n50_s50_long_manager,
                      hrp_weak_vol_ewa_r025_n50_s50_l10_long_manager,
                      hrp_weak_vol_ewa_r001_n200_s50_l20_long_manager]
HRP_LS_MANAGERS = []
HRP_MANAGERS = HRP_LONG_MANAGERS + HRP_LS_MANAGERS