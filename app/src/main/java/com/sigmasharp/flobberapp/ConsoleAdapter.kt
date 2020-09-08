package com.sigmasharp.flobberapp

import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.console_item_row.view.*

class ConsoleAdapter(private val items: ArrayList<String>) :
    RecyclerView.Adapter<ConsoleAdapter.ConsoleItemHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ConsoleAdapter.ConsoleItemHolder {
        val inflatedView = parent.inflate(R.layout.console_item_row, false)
        return ConsoleItemHolder(inflatedView)
    }

    override fun getItemCount(): Int = items.size

    override fun onBindViewHolder(holder: ConsoleAdapter.ConsoleItemHolder, position: Int) {
        holder.bindText(items[position])
    }

    class ConsoleItemHolder(v: View) : RecyclerView.ViewHolder(v) {
        private var view: View = v
        private var item: String? = null

        fun bindText(text:String){
            view.consoleItem.text=text
        }
    }

}
