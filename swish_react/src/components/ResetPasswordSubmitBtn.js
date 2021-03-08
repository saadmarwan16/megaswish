import React from 'react'

const ResetPasswordSubmitBtn = () => {
    const onSubmit = (e) => {
        e.preventDefault()
    }
    
    return (
        <>
            <input type="submit" value="Reset" className="btn btn-primary form-submit-btn" onSubmit={onSubmit} />
        </>
    )
}

export default ResetPasswordSubmitBtn