
def ft_tqdm(lst: range) -> None:
    """
    This function takes a range and prints a progress bar of the iteration.

    Parameters:
        lst (range): The range to iterate over.

    Returns:
        None
    """

    try:
        assert isinstance(lst, range), "bad arguments"

        bar_len = 70

        i_total_len = len(lst)
        for i in lst:

            i_progress_percent = int((i + 1) / i_total_len * 100)
            i_position = int((i + 1) / i_total_len * bar_len)
            s_progress_bar = '█' * i_position

            print(
                f"\r{i_progress_percent}%"
                f"|{s_progress_bar:<{bar_len}}| {i + 1}/{i_total_len}", end='')

            yield i

        print()

    except AssertionError as e:
        print("AssertionError:", e)
    except ValueError:
        pass
