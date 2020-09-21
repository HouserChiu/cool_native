# coding: utf-8

import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """
Java.perform(function () {
    var pointer = Module.findBaseAddress("libnative-lib.so").add(0x66740 + 1);
    console.log('first_md5 pointer:', pointer);

    Interceptor.attach(pointer, {
        onEnter: function (args) {
            console.log('v65:', args[0]);
            console.log('s:', Memory.readCString(args[1]));
            console.log('v41:', parseInt(args[2]));
            console.log('----------------');
        },
        onLeave: function (retval) {
        }
    })
})

Java.perform(function () {
    var pointer = Module.findBaseAddress("libnative-lib.so").add(0x66814 + 1);
    console.log('base64:', pointer);

    Interceptor.attach(pointer, {
        onEnter: function (args) {
            console.log('v49:', Memory.readCString(args[0]));
            console.log('----------------');
        },
        onLeave: function (retval) {
        }
    })
})

Java.perform(function () {
    var pointer = Module.findBaseAddress("libnative-lib.so").add(0x6682E + 1);
    console.log('second_md5 pointer:', pointer);

    Interceptor.attach(pointer, {
        onEnter: function (args) {
            console.log('v58:', args[0]);
            console.log('v52:', Memory.readCString(args[1]));
            console.log('v53:', parseInt(args[2]));
            console.log('----------------');
        },
        onLeave: function (retval) {
        }
    })
})

"""

process = frida.get_usb_device().attach('com.coolapk.market')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()
