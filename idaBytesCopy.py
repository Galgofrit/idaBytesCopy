import subprocess

def pbcopy(contents):
    subprocess.run('/usr/bin/pbcopy', input=contents)

start = idc.read_selection_start()
end = idc.read_selection_end()

print(hex(start), hex(end))

contents = ''

while start < end: 
    contents += hex(idc.get_wide_byte(start))
    start = ida_bytes.next_addr(start)

contents = ''.join(['0' + byte if len(byte) == 1 else byte for byte in contents.split('0x')])
pbcopy(bytes(contents, 'utf8'))
