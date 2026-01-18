def format_name(f_name, l_name):
    # print(f_name.title())
    # print(l_name.title())
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return f"{formatted_fname} {formatted_lname}"

formatted_string = format_name(f_name='rugved', l_name='wakekar')
print(formatted_string)