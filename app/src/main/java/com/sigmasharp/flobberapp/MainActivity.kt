package com.sigmasharp.flobberapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.LinearLayoutManager
import com.sigmasharp.flobberapp.services.console.ConsoleItemType
import com.sigmasharp.flobberapp.services.console.ConsoleService
import com.sigmasharp.flobberapp.services.console.MemoryConsoleService
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    private lateinit var linearLayoutManager: LinearLayoutManager
    private lateinit var consoleAdapter: ConsoleAdapter
    private lateinit var consoleService: ConsoleService

    override fun onCreate(savedInstanceState: Bundle?) {
        consoleService=MemoryConsoleService()

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        linearLayoutManager = LinearLayoutManager(this)
        rvConsole.layoutManager = linearLayoutManager
        consoleAdapter = ConsoleAdapter(consoleService.getItems())
        rvConsole.adapter = consoleAdapter
        log("Application Initialized")
        log("Application Initialized",ConsoleItemType.Warning)
        log("Application Initialized",ConsoleItemType.Error)
    }

    private fun log(content:String,type:ConsoleItemType=ConsoleItemType.Normal){
        consoleService.log(content,type)
        consoleAdapter.notifyItemInserted(consoleService.getItems().size-1)
    }
}