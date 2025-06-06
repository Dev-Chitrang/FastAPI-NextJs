"use client"

import { useContext, useEffect, useState } from "react"
import { useRouter } from "next/navigation"
import AuthContext from "../context/AuthContext"

const ProtectedRouter = ({ children }) => {
    const { user } = useContext(AuthContext)
    const router = useRouter()

    useEffect(() => {
        if (!user) {
            router.push('/login')
        }
    }, [user, router])

    return user ? children : null
}

export default ProtectedRouter