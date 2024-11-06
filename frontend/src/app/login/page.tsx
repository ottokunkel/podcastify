'use client';

import { Button } from "@/components/ui/button";
import { redirect } from 'next/navigation';
import { signIn, getSession } from "@/tools/auth";
import { useState } from 'react';

export default function Home() {
    const [error, setError] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    // Check session client-side
    const checkSession = async () => {
        const { data: { session } } = await getSession();
        if (session) {
            // Set authorization header with access token
            if (session.access_token) {
                localStorage.setItem('authToken', session.access_token);
            }
            redirect('/');
        }
    };
    checkSession();

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        setError("");

        const result = await signIn(email, password);
        if (!result.success) {
            setError(result.error ?? "");
            return;
        }

        // Set authorization header with access token after successful login
        if (result.data?.session?.access_token) {
            localStorage.setItem('authToken', result.data.session.access_token);
        }

        // Redirect on successful login
        redirect('/');
    };

    return (
        <>
            <div className="flex-1 bg-slate-100 flex items-center justify-center">
                <form onSubmit={handleLogin} className="w-[600px] rounded-lg h-[300px] flex p-5 bg-slate-200 flex-col justify-between">
                    <h1 className="text-2xl font-bold">Login</h1>
                    {error && <p className="text-red-500">{error}</p>}
                    <div className="flex flex-col gap-5">
                        <input 
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            placeholder="Email" 
                            className="p-2 rounded-md" 
                        />
                        <input 
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            placeholder="Password" 
                            className="p-2 rounded-md" 
                            type="password" 
                        />
                    </div>
                    <Button type="submit" className="align-bottom">
                        Login 
                    </Button>
                </form>
            </div>  
        </>
    );
}