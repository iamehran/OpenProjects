import { configureStore } from "@reduxjs/toolkit";
import digitsReducer from './features/digitSlice'
import themeReducer from './features/ToggleSlice'



//creating the store
export const store =configureStore({

    reducer:{

        digits:digitsReducer,
        theme:themeReducer

    }
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch