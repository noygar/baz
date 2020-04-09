import matplotlib.patheffects as path_effects
import pylab as plt
import random
from matplotlib import rc

_chars = "ijkmnxyzacbde"
_vals = [i for i in range(0, 10)]

sim_ops = ["+", "-"]
all_ops = ["+", "-", "/", "x"]


def create_var(chars=_chars, vals=_vals, coin=True):
    if coin:
        char = random.choice(chars)
        return char
    else:
        val = random.choice(vals)
        return str(val)


def create_op(var1, var2):
    op = random.choice(all_ops)
    if op == "+":
        return var1 + "+" + var2
    elif op == '-':
        use_braces = random.choice([True, False])
        if use_braces:
            braces = random.choice([("\\left(", "\\right)"), ("\\left[", "\\right]"), ("\\left|", "\\right|")])
            return braces[0]+var1 + "-" + var2 + braces[1]
        else:
            return var1 + "-" + var2
    elif op == "x":
        return mul_op(var1, var2)
    elif op == "/":
        return div_op(var1, var2)


def div_op(var1, var2):
    return "\\displaystyle\\frac{" + var1 + "}" + "{" + var2 + "}"


def mul_op(var1, var2):
    return var1 + "\\cdot" + "{" + var2 + "}"


def create_eq(max_block=2, max_var_size=2):
    latex_list = []
    for _ in range(max_block):
        var1 = create_var()
        for _ in range(max_var_size):
            var2 = create_var(coin=False)
            var1 = create_op(var1, var2)
        latex_list.append(var1)

    for ind, latex in enumerate(latex_list):
        if ind == 0:
            block = latex
            continue
        block = create_op(block, latex)
    return block

lat = "\\frac{x+2\\times{6}-\\frac{n}{9}+3}{\\frac{z\\times{9}}{0}}"


def show_eq():
    rc('text', usetex=True)
    plt.rcParams['text.latex.preamble'] = [
        r'\usepackage{tgheros}',  # helvetica font
        r'\usepackage{sansmath}',  # math-font matching  helvetica
        r'\sansmath',  # actually tell tex to use it!
        r'\usepackage{siunitx}',  # micro symbols
        r'\sisetup{detect-all}',  # force siunitx to use the fonts
    ]
    for _ in range(100):
        fig = plt.figure(figsize=(7, 3))
        latex = create_eq()
        txte = r"$$\mathrm{" + latex + "}$$"

        text = fig.text(0.5, 0.5, txte, ha='center', va='center', size=30)
        text.set_path_effects([path_effects.Normal()])
        plt.show()


def show_eq_mono(latex):
    rc('text', usetex=True)
    plt.rcParams['text.latex.preamble'] = [
        r'\usepackage{tgheros}',  # helvetica font
        r'\usepackage{sansmath}',  # math-font matching  helvetica
        r'\sansmath',  # actually tell tex to use it!
        r'\usepackage{siunitx}',  # micro symbols
        r'\sisetup{detect-all}',  # force siunitx to use the fonts
    ]
    fig = plt.figure(figsize=(7, 3))
    txte = r"$$\mathrm{" + latex + "}$$"
    text = fig.text(0.5, 0.5, txte, ha='center', va='center', size=30)
    text.set_path_effects([path_effects.Normal()])
    plt.show()


def show_eq():
    rc('text', usetex=True)
    plt.rcParams['text.latex.preamble'] = [
        r'\usepackage{tgheros}',  # helvetica font
        r'\usepackage{sansmath}',  # math-font matching  helvetica
        r'\sansmath',  # actually tell tex to use it!
        r'\usepackage{siunitx}',  # micro symbols
        r'\sisetup{detect-all}',  # force siunitx to use the fonts
    ]
    for _  in range(100):
        latex = create_eq()
        fig = plt.figure(figsize=(7, 3))
        txte = r"$$\mathrm{" + latex + "}$$"
        text = fig.text(0.5, 0.5, txte, ha='center', va='center', size=30)
        text.set_path_effects([path_effects.Normal()])
        plt.show()

show_eq()

