package tech.karonty.jetnote

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.material.MaterialTheme
import androidx.compose.material.Surface
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.ExperimentalComposeUiApi
import androidx.compose.ui.tooling.preview.Preview
import androidx.lifecycle.viewmodel.compose.viewModel
import dagger.hilt.android.AndroidEntryPoint
import tech.karonty.jetnote.screen.NoteScreen
import tech.karonty.jetnote.screen.NoteViewModel
import tech.karonty.jetnote.ui.theme.JetNoteTheme

@ExperimentalComposeUiApi
@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            JetNoteTheme {
                // A surface container using the 'background' color from the theme
                Surface(color = MaterialTheme.colors.background) {
                    //val noteViewModel = viewModel<NoteViewModel>() //also works
                    val noteViewModel = viewModel<NoteViewModel>()
                    NotesApp(noteViewModel)

                }
            }
        }
    }
}

@ExperimentalComposeUiApi
@Composable
fun NotesApp(noteViewModel: NoteViewModel) {
    val notesList = noteViewModel.noteList.collectAsState().value

    NoteScreen(notes = notesList,
        onRemoveNote = { noteViewModel.removeNote(it) },
        onAddNote = { noteViewModel.addNote(it) })

}


@ExperimentalComposeUiApi
@Preview(showBackground = true)
@Composable
fun DefaultPreview() {
    JetNoteTheme {
        val noteViewModel = viewModel<NoteViewModel>()
        NotesApp(noteViewModel)
    }
}