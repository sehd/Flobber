package com.sigmasharp.flobberapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.LinearLayoutManager
import com.sigmasharp.flobberapp.services.bluetooth.BlueTooth
import com.sigmasharp.flobberapp.services.bluetooth.BlueToothImpl
import com.sigmasharp.flobberapp.services.logger.LogAddedCallback
import com.sigmasharp.flobberapp.services.logger.LogItemType
import com.sigmasharp.flobberapp.services.logger.Logger
import com.sigmasharp.flobberapp.services.logger.MemoryLogger
import com.sigmasharp.flobberapp.services.messaging.Messaging
import com.sigmasharp.flobberapp.services.messaging.SimpleMessaging
import com.sigmasharp.flobberapp.services.web.KtorWebServer
import com.sigmasharp.flobberapp.services.web.WebServer
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    private lateinit var linearLayoutManager: LinearLayoutManager
    private lateinit var consoleAdapter: ConsoleAdapter

    private lateinit var logger: Logger
    private lateinit var messaging: Messaging
    private lateinit var webServer: WebServer
    private lateinit var bluetooth: BlueTooth
    private lateinit var flobber: Flobber

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        //Configuration
        val port = 8080

        //Dependencies
        logger = MemoryLogger()
        messaging = SimpleMessaging(logger)
        webServer = KtorWebServer(logger, messaging)
        bluetooth = BlueToothImpl(logger)
        flobber = Flobber(logger, messaging, bluetooth)

        startLogger()

        try {
            logger.log("Booting...")
            webServer.start(port)
            bluetooth.start()
            flobber.start()
            logger.log("Application Initialized")
        } catch (ex: Exception) {
            logger.log("Failed to load application: " + ex.message, LogItemType.Error)
        }
    }

    private fun startLogger() {
        setContentView(R.layout.activity_main)
        linearLayoutManager = LinearLayoutManager(this)
        rvConsole.layoutManager = linearLayoutManager
        consoleAdapter = ConsoleAdapter(logger.getItems())
        rvConsole.adapter = consoleAdapter
        logger.setLogAddedCallBack {
            consoleAdapter.notifyItemInserted(logger.getItems().size - 1)
        }
    }
}