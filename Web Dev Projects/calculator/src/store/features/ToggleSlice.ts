import { createSlice  } from "@reduxjs/toolkit";



interface ToggleState {

    darkTheme:boolean

}


const initialState : ToggleState={
    darkTheme:false
}

//Toggle Slice in the redux toolkit
export const ToggleSlice = createSlice({

    name:"ToggleState",
    initialState,
    reducers:{
        setDarkTheme:(state)=>{
            return {
                ...state,
                darkTheme:true

            }
        }
        
    }
})


export const {setDarkTheme}= ToggleSlice.actions

export default ToggleSlice.reducer