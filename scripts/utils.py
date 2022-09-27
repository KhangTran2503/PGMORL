import os

def get_n_experiment(parent_dir, env_name,method):
    """Return maximum number of experiments in folder.
    Finds the highest run number and return number + 1.
    Parameters
    ----------
    parent_dir: str
    'results/env_name/method/n_experiment/..'
      Path of the directory containing all experiment runs.
    Returns
    -------
      number of experiment
    """
    # file 'results/env_name/method/n_experiment/..'
    #os.makedirs(parent_dir, exist_ok=True)
    experiment_id = -1
    if not os.path.exists(parent_dir):
        return experiment_id
    if not os.path.isdir(os.path.join(parent_dir,env_name)):
        return experiment_id

    cur_dir = os.path.join(parent_dir,env_name)
    if not os.path.isdir(os.path.join(cur_dir,method)):
        return experiment_id

    cur_dir = os.path.join(cur_dir,method)

    for folder_name in os.listdir(cur_dir):
        if not os.path.isdir(os.path.join(cur_dir, folder_name)):
            continue
        try:
            #print(cur_dir,folder_name)
            folder_name = int(folder_name)
            if folder_name > experiment_id:
                experiment_id = folder_name
        except:
            pass
    #experiment_id += 1
    return experiment_id


def get_method(args):
    if args.pgmorl:
        return 'pgmorl'
    if args.ra:
        return 'ra'
    if args.random:
        return 'random'
    if args.pfa:
        return 'pfa'
    if args.moead:
        return 'moead'
    raise "Don't have this method"