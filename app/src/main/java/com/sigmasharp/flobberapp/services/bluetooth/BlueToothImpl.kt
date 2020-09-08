package com.sigmasharp.flobberapp.services.bluetooth

import com.sigmasharp.flobberapp.services.logger.Logger

class BlueToothImpl(private val logger: Logger) : BlueTooth {
    override fun start() {
        TODO("Not yet implemented")
    }

    override fun send(message: String) {
        logger.addWarning("Not sending $message")
    }

}