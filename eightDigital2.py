
g_dict_layouts = {}
g_dict_shifts = {0:[1, 3], 1:[0, 2, 4], 2:[1, 5],
                 3:[0,4,6], 4:[1,3,5,7], 5:[2,4,8],
                 6:[3,7],  7:[4,6,8], 8:[5,7]}


def swap_chr(a, i, j):
    if i > j:
        i, j = j, i
    b = a[:i] + a[j] + a[i+1:j] + a[i] + a[j+1:]
    return b


def solvePuzzle_span(srcLayout, destLayout):

    g_dict_layouts = {}
    g_dict_shifts = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
                     3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
                     6: [3, 7], 7: [4, 6, 8], 8: [5, 7]}
    g_dict_layouts[srcLayout] = -1

    stack_layouts = []
    stack_layouts.append(srcLayout)
    i = 0
    try:
        bFound = False
        while len(stack_layouts) > 0:
            curLayout = stack_layouts[i]
            if curLayout == destLayout:
                bFound = True
                break
            i = i + 1
            # 寻找0 的位置。
            ind_slide = curLayout.index("0")
            lst_shifts = g_dict_shifts[ind_slide]
            for nShift in lst_shifts:
                newLayout = swap_chr(curLayout, nShift, ind_slide)

                if g_dict_layouts.get(newLayout) == None:
                    g_dict_layouts[newLayout] = curLayout
                    stack_layouts.append(newLayout)
    except:
        print("布局不可达！")

    if bFound:
        lst_steps = []
        lst_steps.append(curLayout)
        while g_dict_layouts[curLayout] != -1:
            curLayout = g_dict_layouts[curLayout]
            lst_steps.append(curLayout)
        lst_steps.reverse()
        return 0, lst_steps
    else:
        return -1, None


if __name__ == "__main__":
    #srcLayout  = "213456780"
    #destLayout = "213056478"

    # srcLayout  = "835127460"
    # destLayout = "835107462"
    srcLayout  = "203184765"
    destLayout = "234108765"
    # srcLayout  = "541203786" #""013425786"
    # destLayout = "123804765" #"647850321"

    retCode, lst_steps = solvePuzzle_span(srcLayout, destLayout)
    print(retCode)
    print(lst_steps)
    if retCode != 0:
        print("目标布局不可达")
    else:

        for nIndex in range(len(lst_steps)):
            print("step #" + str(nIndex + 1))
            print(lst_steps[nIndex][:3])
            print(lst_steps[nIndex][3:6])
            print(lst_steps[nIndex][6:])