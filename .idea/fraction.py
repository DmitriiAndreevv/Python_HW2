def fraction_proc(frac_str, frac_sstr):
    num1, num2 = map(int, frac_str.split("/"))
    num3, num4 = map(int, frac_str.split("/"))

    frac_num = num1 * num2 + num3 * num4
    frac_num2 = num2 * num4
    frac = (frac_num, frac_num2)

    proc_frac = num1 * num3
    proc_frac2 = num2 * num4
    proc_frac_res = (proc_frac, proc_frac2)

    return frac, proc_frac_res


frac_str = "2/2"
frac_sstr = "2/2"

frac, proc_frac_res = fraction_proc(frac_str, frac_sstr)

print(f"Сумма дробей: {frac_str} and {frac_sstr} - {frac[0]}/{frac[1]}")
print(f"Произведение дробей: {frac_str} and {frac_sstr} - {proc_frac_res[0]}/{proc_frac_res[1]}")
