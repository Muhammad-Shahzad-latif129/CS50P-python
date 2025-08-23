months = [
    "January","February","March","April","May","June","July","August",
    "September","October","November","December"
]

def main():
    while True:
        try:
            s = input("Date: ").strip()
            m, d, y = s.split(sep="/")
            m, d, y = int(m), int(d), int(y)
            if 1 <= m <= 12 and 1 <= d <= 31:
                print(f"{y}-{m:02}-{d:02}")
                break
        except ValueError:
            pass    

        try:
            m_name, d_comma, yy = s.split(" ")  
            dd = d_comma.rstrip(',') 
            if m_name.capitalize() in months:
                mm = months.index(m_name.capitalize()) + 1
                dd, yy = int(dd), int(yy)
                if 1 <= dd <= 31:
                    print(f"{yy}-{mm:02}-{dd:02}")
                    break
        except ValueError:
            pass            
main()    