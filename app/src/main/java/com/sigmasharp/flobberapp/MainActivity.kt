package com.sigmasharp.flobberapp

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.sigmasharp.flobberapp.services.logger.Logger
import com.sigmasharp.flobberapp.services.logger.MemoryLogger
import kotlinx.android.synthetic.main.activity_main.*
import kotlin.concurrent.thread

class MainActivity : AppCompatActivity() {
    private lateinit var linearLayoutManager: LinearLayoutManager
    private lateinit var consoleAdapter: ConsoleAdapter
    private lateinit var logger: Logger

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        logger = MemoryLogger()
        startLogger()
        val bootstrapper = FlobberBootstrapper(application, logger)
        thread { bootstrapper.bootstrap() }
    }

    private fun startLogger() {
        setContentView(R.layout.activity_main)
        linearLayoutManager = LinearLayoutManager(this)
        rvConsole.layoutManager = linearLayoutManager
        consoleAdapter = ConsoleAdapter(logger.getItems())
        rvConsole.adapter = consoleAdapter
        logger.setLogAddedCallBack {
            this@MainActivity.runOnUiThread {
                consoleAdapter.notifyItemChanged(it)
            }
        }
    }
}