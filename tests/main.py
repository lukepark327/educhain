from time import sleep

if __name__ == '__main__':
    tests = []

    # import test cases
    from test1 import main as test1
    tests.append(test1)

    """
    Run test(s)
    """
    pass_cnt = 0
    total_cnt = 0

    for test in tests:
        pass_cnt_per_test, total_cnt_per_test = test.scenario()
        pass_cnt += pass_cnt_per_test
        total_cnt += total_cnt_per_test

        sleep(1)

    # print test results
    print("")
    print(str(pass_cnt) + " / " + str(total_cnt) + " tests pass")
