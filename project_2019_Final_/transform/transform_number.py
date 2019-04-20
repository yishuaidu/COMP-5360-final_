"""
A module for working with zip code data
Copyright Yihshuai
"""


def clean_comma(pd):
    """
    clean comma from a str
    Input: pd type
    return: pd type
    """
    return pd.str.replace(",", "")



def convert_k(value):
    """
    For conver k, such as 10k to 10000
    Input: str
    return: int
    """
    if value:
        time = 1
        if value.endswith("k"):
            time = 1000
            value = value[0:len(value)-1]
        return int(float(value) * time)

def convert_dollar(pd):
    """
    convert all values with $ to int in pd type
    input: pd
    reutrn: pd
    """
    pd = pd.apply(lambda x:x.split('.')[0].strip())
    pd = clean_comma(pd)
    pd = pd.str.replace("$","")
    return  pd.astype("int")

def normalize(x, y):
    """
    Normalize between 0-1
    input: pd
    return:pd
    """
    return x.astype("float")/y.astype("float")