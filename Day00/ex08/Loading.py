def ft_tqdm(lst: range) -> None:
    '''
    ft_tqdm(lst: range) --> None

    Print a progress bar of the iteration over the range object lst.
    '''

    for i in lst:
        percent = (i+1)*100//lst.stop
        print(f"\r{percent: >3}%|{'█'*(percent)}{' '*(100-percent)}\
| {i+1}/{lst.stop}", end="")
        yield
