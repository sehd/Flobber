package com.sigmasharp.flobberapp.services.web

import android.content.Context
import com.sigmasharp.flobberapp.services.messaging.MessageAddress

interface WebServer {
    companion object {
        val moveForwardRequested = MessageAddress("WebServer_moveForwardRequested")
        val moveBackwardRequested = MessageAddress("WebServer_moveBackwardRequested")
        val moveLeftRequested = MessageAddress("WebServer_moveLeftRequested")
        val moveRightRequested = MessageAddress("WebServer_moveRightRequested")
        val moveStopRequested = MessageAddress("WebServer_moveStopRequested")
    }

    fun start(port: Int, context: Context)
}