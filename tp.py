import sp
import wi

SYMBOLS = ['C', 'W', 'S', 'SM', 'BO']
MONTH_LETTERS = {'JAN': 'F',
                 'FEB': 'G',
                 'MAR': 'H',
                 'APR': 'J',
                 'MAY': 'K',
                 'JUN': 'M',
                 'JLY': 'N',
                 'AUG': 'Q',
                 'SEP': 'U',
                 'OCT': 'V',
                 'NOV': 'X',
                 'DEC': 'Z'}
                 

def make_header():
    header = "%report.text - the python output for tex rendering.\n"
    header += "\\documentclass{article}\n"
    header += "\\usepackage{times}\n"
    header += "\\usepackage[margin=1cm]{geometry}\n"
    header += "\\usepackage{array}\n"
    header += "\\usepackage{caption}\n"
    header += "\\begin{document}\n"
    header += "\\title{Options Open Interest}\n"
    header += "\\date{\\today}\n"
    header += "\\maketitle\n"
    header += "\\begin{table}[h!]\n"
    header += "\\centering\n"
    header += "\\begin{tabular}{| r | r | r | r | r | r |}\n"
    header += "\\hline\n"
    header += "Contract & Delta Equivalent & Change & Avg Call & Avg Put & Avg Option\n"
    header += "\\\\\n"
    header += "\\hline\n"
    header += "& & & & & \\\\\n"
    header += "\\hline\n"

    return header


def make_footer():
    footer = "\\hline\n"
    footer += "\\end{tabular}\n"
    footer += "\\caption{This table shows \\newline 1) the futures equivalent open interest in options on a delta weighted basis. \newline 2) the simple average open interest for calls, puts, and combined positions.}\n"
    footer += "\\end{table}\n"
    footer += "\\end{document}\n"

    return footer


def month_line(symbol, month):

    month_abbreviation = MONTH_LETTERS[month[:3]]
    month_abbreviation += month[-1]
    
    (futures, options) = sp.get_all_options(symbol)
    average_options = wi.get_average_option(options[month])
    total_delta = wi.calc_total_greek(options[month], 'delta')
    
    line = "{0}{1} & {2:,.0f} &   & {3:.0f} & {4:.0f} & {5:.0f}\\\\\n".format(
        symbol,
        month_abbreviation,
        total_delta,
        average_options["CALL"],
        average_options["PUT"],
        average_options["TOTAL"])

    return line


def main():
    header = make_header()
    S_NOV16 = month_line('S', 'NOV16')
    footer = make_footer()
    print("{0}{1}{2}".format(header, S_NOV16, footer))

    
if __name__ == '__main__':
    main()