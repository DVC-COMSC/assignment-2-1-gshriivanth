def main():
    
    m_num = int(input("Enter the number of male students in your class: "))
    f_num = int(input("Enter the number of female students in your class: "))
    total = m_num + f_num

    m_perc = (m_num / total) * 100
    f_perc = (f_num / total) * 100

    print(f"Total number of students: {total}")
    print("Number of males and females:", str(m_num), str(f_num), sep = '\t')
    print("The percentage of males and females:\t", format(m_perc, '.2f'), "%\t", format(f_perc, '.2f'), "%")

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
