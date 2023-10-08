package tech.karonty.jetnote.screen

import android.util.Log
import android.widget.Toast
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.Notifications
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import tech.karonty.jetnote.R
import tech.karonty.jetnote.components.NoteButton
import tech.karonty.jetnote.components.NoteInputText
import tech.karonty.jetnote.data.NotesDataSource
import tech.karonty.jetnote.model.Note
import java.time.format.DateTimeFormatter

@ExperimentalComposeUiApi
@Composable
fun NoteScreen(
    notes: List<Note>,
    onAddNote: (Note) -> Unit,
    onRemoveNote: (Note) -> Unit
){

    var title by remember{
        mutableStateOf("")
    }

    var description by remember{
        mutableStateOf("")
    }

    val context = LocalContext.current

    Column(
        modifier = Modifier
            .padding(6.dp)
    ) {
        TopAppBar(
            title = {
                Text(text = stringResource(id = R.string.app_name))
            },
            actions = {
                Icon(
                    imageVector = Icons.Rounded.Notifications,
                    contentDescription = "Icon"
                )
            },
            backgroundColor = Color(0xFFDADFE3)
        )


        // CONTENT

        Column(
            modifier = Modifier
                .fillMaxWidth(),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            NoteInputText(
                modifier = Modifier
                    .padding(
                        top = 9.dp,
                        bottom = 8.dp
                    ),
                text = title,
                label = stringResource(id = R.string.title_label),
                onTextChane = {
                    if (it.all {  char ->
                        char.isLetter() || char.isWhitespace()
                        }
                    ){
                        title = it
                    }
                }
            )

            NoteInputText(
                modifier = Modifier
                    .padding(
                        top = 9.dp,
                        bottom = 8.dp
                    ),
                text = description,
                label = stringResource(id = R.string.desc_label),
                onTextChane = {
                    if (it.all {  char ->
                            char.isLetter() || char.isWhitespace()
                        }
                    ){
                        description = it
                    }
                }
            )
            
            NoteButton(
                text = stringResource(id = R.string.save_button_label),
                onClick = {
                    if (title.isNotEmpty() && description.isNotEmpty()){
                        onAddNote(
                            Note(
                                title = title,
                                description = description
                            )
                        )
                        title = ""
                        description = ""
                        Toast.makeText(context, "Note Add", Toast.LENGTH_LONG).show()
                    }
                }
            )
        }

        Divider(
            modifier = Modifier
                .padding(10.dp)
        )
        
        LazyColumn(
            
        ){
            items(notes) { note ->
                NoteRow(
                    note = note ,
                    onNoteClicked = {
                        onRemoveNote(note)
                    }
                )
            }
        }

    }
}


@Composable
fun NoteRow(
    modifier: Modifier = Modifier,
    note: Note,
    onNoteClicked: (Note) -> Unit
){
    Surface(
        modifier
            .padding(4.dp)
            .clip(
                RoundedCornerShape(
                    topEnd = 33.dp,
                    bottomStart = 33.dp
                )
            )
            .fillMaxWidth(),
        color = Color(0XFFDFE6EB),
        elevation = 6.dp
    ) {
        Column(
            modifier
                .clickable {
                    onNoteClicked(note)
                }
                .padding(
                    horizontal = 14.dp,
                    vertical = 6.dp
                ),
            horizontalAlignment = Alignment.Start
        ) {
            Text(
                text = note.title,
                style = MaterialTheme.typography.subtitle2
            )

            Text(
                text = note.description,
                style = MaterialTheme.typography.subtitle1
            )

//            Text(
//                text = note.entryDate.format(
//                    DateTimeFormatter.ofPattern("EEE, d MMM")
//                ),
//                style = MaterialTheme.typography.caption
//            )
        }
    }
}

@ExperimentalComposeUiApi
@Preview(showBackground = true)
@Composable
fun NoteScreenPreview(){
    NoteScreen(
        notes = NotesDataSource().loadNotes(),
        onAddNote = {

        },
        onRemoveNote = {

        }
    )
}