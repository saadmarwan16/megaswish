import React, { useState, useEffect } from 'react'

const PasswordSpecsIndicator = () => {

    const [password, setPassword] = useState(() => '')
    const [confirmation, setConfirmation] = useState(() => '')

    const [isCharSpecTrue, setIsCharSpecTrue] = useState(() => false)
    const checkCharSpecStatus = () => setIsCharSpecTrue(/(?=.{8,}$)/.test(password))

    const [isDigitSpecTrue, setIsDigitSpecTrue] = useState(() => false)
    const checkDigitSpecStatus = () => setIsDigitSpecTrue(/(?=.*[0-9])/.test(password))

    const [isMatchSpecTrue, setIsMatchSpecTrue] = useState(() => false)
    const checkMatchSpecStatus = () => setIsMatchSpecTrue(password === confirmation)

    const [isUpperSpecTrue, setIsUpperSpecTrue] = useState(() => false)
    const checkUpperSpecStatus = () => setIsUpperSpecTrue(/(?=.*[A-Z])/.test(password))

    const [isLowerSpecTrue, setIsLowerSpecTrue] = useState(() => false)
    const checkLowerSpecStatus = () => setIsLowerSpecTrue(/(?=.*[a-z])/.test(password))

    const [isSpecialSpecTrue, setIsSpecialSpecTrue] = useState(() => false)
    const checkSpecialSpecStatus = () => setIsSpecialSpecTrue(/(?=.*\W)/.test(password))

    useEffect(() => {
        if (password.length > 0 || confirmation.length > 0) {
            checkSpecs()
        } else {
            checkCharSpecStatus()
            checkDigitSpecStatus()
            checkUpperSpecStatus()
            checkLowerSpecStatus()
            checkSpecialSpecStatus()
        }
    }, [password, confirmation])

    const checkSpecs = () => {
        checkCharSpecStatus()
        checkDigitSpecStatus()
        checkMatchSpecStatus()
        checkUpperSpecStatus()
        checkLowerSpecStatus()
        checkSpecialSpecStatus()
    }

    const onPasswordChange = (e) => setPassword(e.target.value)

    const onConfirmationChange = (e) => setConfirmation(e.target.value)

    return (
        <>
            <div className="form-group">
                <input autoFocus required className="form-control" type="password" name="password"
                    placeholder="Enter Password" onChange={onPasswordChange} value={password}
                />
            </div>

            <div className="form-group">
                <input required className="form-control" type="password" name="confirm-password"
                    placeholder="Password Again" onChange={onConfirmationChange} value={confirmation}
                />
            </div>

            <div className="container-fluid form-group">
                <div className="row">
                    <div className="col-md-6 col-12 password-specs-container">
                        <ul className="password-specs-list">
                            <li className={isCharSpecTrue ? 'password-specs-list-item' : null}>
                                At least 8 characters long
                            </li>
                            <li className={isDigitSpecTrue ? 'password-specs-list-item' : null}>
                                At least 1 digit
                            </li>
                            <li className={isMatchSpecTrue ? 'password-specs-list-item' : null}>
                                Passwords must match
                            </li>
                        </ul>
                    </div>

                    <div className="col-md-6 col-12 password-specs-container">
                        <ul className="password-specs-list">
                            <li className={isUpperSpecTrue ? 'password-specs-list-item' : null}>
                                At least 1 uppercase
                            </li>
                            <li className={isLowerSpecTrue ? 'password-specs-list-item' : null}>
                                At least 1 lowercase
                            </li>
                            <li className={isSpecialSpecTrue ? 'password-specs-list-item' : null}>
                                At least 1 special character
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </>
    )
}

export default PasswordSpecsIndicator