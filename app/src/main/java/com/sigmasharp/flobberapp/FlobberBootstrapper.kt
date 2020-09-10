package com.sigmasharp.flobberapp

import android.app.Application
import com.sigmasharp.flobberapp.services.bluetooth.BlueTooth
import com.sigmasharp.flobberapp.services.bluetooth.BlueToothImpl
import com.sigmasharp.flobberapp.services.logger.LogItemType
import com.sigmasharp.flobberapp.services.logger.Logger
import com.sigmasharp.flobberapp.services.messaging.Messaging
import com.sigmasharp.flobberapp.services.messaging.SimpleMessaging
import com.sigmasharp.flobberapp.services.web.KtorWebServer
import com.sigmasharp.flobberapp.services.web.WebServer

class FlobberBootstrapper(
    private val application: Application,
    private val logger: Logger
) {
    private lateinit var messaging: Messaging
    private lateinit var webServer: WebServer
    private lateinit var bluetooth: BlueTooth
    private lateinit var flobber: Flobber

    init {
        defineDependencies()
    }

    fun bootstrap() {
        startServices()
    }

    private fun defineDependencies() {
        messaging = SimpleMessaging(logger)
        webServer = KtorWebServer(logger, messaging, application.assets)
        bluetooth = BlueToothImpl(logger)
        flobber = Flobber(logger, messaging, bluetooth)
    }

    private fun startServices() {
        try {
            logger.log("Booting...")
            webServer.start(Config.port, application.applicationContext)
            bluetooth.start()
            flobber.start()
            logger.log("Application Initialized")
        } catch (ex: Exception) {
            logger.log("Failed to load application: " + ex.message, LogItemType.Error)
        }
    }
}