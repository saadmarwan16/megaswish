import React from 'react'
import ReactDOM from 'react-dom'
// import ReactDOM, { BrowserRouter as Router, Switch, Route } from 'react-dom'

import PasswordSpecsIndicator from './components/PasswordSpecsIndicator'
// import ResetPasswordSubmitBtn from './components/ResetPasswordSubmitBtn'
// import ResetPasswordApp from './components/ResetPasswordApp'


ReactDOM.render(
    <React.StrictMode>
        <PasswordSpecsIndicator />
    </React.StrictMode>,
    document.getElementById('register-inputs')
)


// ReactDOM.render(
//     <React.StrictMode>
//         <ResetPasswordApp />
//     </React.StrictMode>,
//     document.getElementById('reset-password-submit-btn')
// )