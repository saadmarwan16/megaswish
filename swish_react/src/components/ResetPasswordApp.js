import React, {useState, useEffect} from 'react'
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from 'react-router-dom'

import PasswordSpecsIndicator from './components/PasswordSpecsIndicator'
import ResetPasswordSubmitBtn from './components/ResetPasswordSubmitBtn'

const App = () => {
    return (
        <>
            <Router>
                <Switch>
                    <Route path='/' exact component={Home} />
                    <Route path='/login' component={Login} />
                    <Route path='/register' exact component={Register} />
                    <Route path='/register/complete' component={RegisterComplete} />
                </Switch>
            </Router>
        </>
    )
}

export default App