package com.sigmasharp.flobberapp.services.bluetooth

import com.sigmasharp.flobberapp.services.messaging.MessageAddress

interface BlueTooth {
    fun start()
    fun send(message: String)

    companion object {
        val bluetoothMessageReceived = MessageAddress("BlueTooth_bluetoothMessageReceived")
    }
}