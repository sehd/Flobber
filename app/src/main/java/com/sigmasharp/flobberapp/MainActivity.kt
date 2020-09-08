package com.sigmasharp.flobberapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.LinearLayoutManager
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
        addConsole("Application Initialized")
    }

    fun addConsole(item:String){
        consoleService.addNormal(item)
        consoleAdapter.notifyItemInserted(consoleService.getItems().size-1)
    }
}