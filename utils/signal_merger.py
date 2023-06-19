import os
import pandas as pd
from pathlib import Path

__all__ = ['signal_merger']

def signal_merger(data_dir, return_id=False):
    """
    Function used to merge all spectrogram signals in a directory

    Parameters:
    ----------
    data_dir : str
        The file location of the spectrogram signals
    return_id : str, optional
        Flags used to include identity columns in output (default is False)

    Return
    ------
    pandas DataFrame
        Spectrogram and glucose level per each sample
    """
    path = Path(data_dir)
    ld = os.listdir(data_dir)
    df_merge = pd.read_excel(os.path.join(data_dir, ld[0]), header=None, index_col=0, engine='openpyxl').T
    df_merge.index = [ld[0].split('.')[0]]
    df_merge['Glucose_level'] = ld[0].split('ng')[0]
    for i, l in enumerate(ld):
        if i == 0:
            pass
        else:
            tmp_d = pd.read_excel(os.path.join(data_dir, l), header=None, index_col=0, engine='openpyxl').T
            tmp_d.index = [l.split('.')[0]]
            tmp_d['Glucose_level'] = [l.split('ng')[0]]
            df_merge = pd.concat([df_merge, tmp_d])

    df_merge = df_merge[['Glucose_level']+df_merge.columns.tolist()[:-1]]
    #df_merge.reset_index(drop=True).to_csv('temp.csv',header=False,index=False)
    if return_id == True:
        df_merge.reset_index().rename(columns={"index": "ID"}).to_csv(os.path.join(path.parents[0],str(path.name)+'_merge_data.csv'))
    else:
        df_merge.reset_index(drop=True).to_csv(os.path.join(path.parents[0],str(path.name)+'_merge_data.csv'),index=False)