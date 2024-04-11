def capture_scope(save_name):
    import pyvisa as visa
    resource_name = "USB0::0xF4EC::0x1103::SDG1XCAC4R0643::INSTR"
    # save_name = "C:\config\ex_capt.bmp" #Make suere that the filepath specified is available on your computer
    _rm = visa.ResourceManager()
    scope = _rm.open_resource(resource_name) #Replace with specific USB information from scope
    scope.write("SCDP")
    result_str = scope.read_raw()
    f = open(save_name,'wb')
    f.write(result_str)
    f.flush()
    f.close()