
def parse_args(expected_args, arg):
    arg_list = arg.split()
    required = [req[0] for req in expected_args]
    if len(arg_list) < len(required):
        print "You are missing a required argument: {}".format(', '.join(required))
        return

    check_arg_types(expected_args, arg_list)

    return arg_list

def check_arg_types(expected_args, arg_list):
    for i, req in enumerate(expected_args):
        if req[1] == str:
            if not check_str(arg_list[i]):
                print "{} must be of type string".format(req[0])

        if req[1] == int:
            if not check_int(arg_list[i]):
                print "{} must be of type integer".format(req[0])

    return arg_list

def check_int(arg):
    try:
        int(arg)
        return True
    except ValueError:
        return False

def check_str(arg):
    return isinstance(arg, basestring)
    #Python 3
    # return isinstance(arg, str)