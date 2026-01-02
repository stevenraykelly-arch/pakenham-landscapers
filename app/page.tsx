import Image from "next/image";
import Link from "next/link";
import { ArrowRight, Check, MapPin, Phone, Star } from "lucide-react";

export default function Home() {
    return (
        <main className="flex min-h-screen flex-col items-center justify-between font-sans text-cyan-950 bg-white">
            {/* Nav */}
            <nav className="fixed top-0 w-full z-50 bg-white/70 backdrop-blur-xl border-b border-cyan-100">
                <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
                    <div className="flex items-center gap-3">
                        <div className="w-12 h-12 bg-cyan-500 rounded-2xl flex items-center justify-center shadow-lg shadow-cyan-200">
                            <Star className="text-white w-7 h-7 fill-current" />
                        </div>
                        <span className="font-black text-2xl tracking-tight text-cyan-950">ST KILDA <span className="text-cyan-500 font-light">WINDOWS</span></span>
                    </div>
                    <Link href="#quote" className="bg-cyan-600 text-white px-8 py-3 rounded-full text-sm font-black uppercase tracking-widest hover:bg-cyan-700 transition-all shadow-lg shadow-cyan-100">
                        Get a Quote
                    </Link>
                </div>
            </nav>

            {/* Hero Section */}
            <section className="relative w-full min-h-screen flex items-center pt-20 overflow-hidden">
                <div className="absolute inset-0 z-0">
                    <div className="w-full h-full bg-[url('/window_cleaner_hero.jpg')] bg-cover bg-center scale-105 active:scale-100 transition-transform duration-1000" />
                    <div className="absolute inset-0 bg-gradient-to-b from-white/20 via-transparent to-white/90" />
                </div>

                <div className="relative z-10 max-w-7xl mx-auto px-6 w-full">
                    <div className="max-w-3xl bg-white/20 backdrop-blur-md p-10 md:p-16 rounded-[40px] border border-white/30 shadow-2xl">
                        <div className="inline-flex items-center gap-2 px-4 py-2 bg-cyan-500 text-white rounded-full text-xs font-black uppercase tracking-widest mb-8 shadow-lg shadow-cyan-200">
                            Crystal Clear Views in 3182
                        </div>
                        <h1 className="text-6xl md:text-9xl font-black text-cyan-950 mb-8 leading-[0.85] tracking-tighter">
                            St Kilda's <br />
                            <span className="text-cyan-600">Purest</span> <br />
                            Finish.
                        </h1>
                        <p className="text-cyan-900/80 text-xl md:text-2xl mb-12 leading-relaxed max-w-xl font-medium">
                            Premium window cleaning for St Kilda's finest apartments and coastal homes. See the bay like never before.
                        </p>

                        <div className="flex flex-col sm:flex-row gap-4">
                            <Link href="#quote" className="px-10 py-5 bg-cyan-600 text-white rounded-2xl font-black text-lg hover:bg-cyan-700 transition-all shadow-xl shadow-cyan-200 flex items-center justify-center gap-3 group">
                                Book Now <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                            </Link>
                            <Link href="tel:0400000000" className="px-10 py-5 bg-white text-cyan-950 border-2 border-cyan-100 rounded-2xl font-black text-lg hover:bg-cyan-50 transition-all flex items-center justify-center gap-3">
                                <Phone className="w-5 h-5" /> 0400 000 000
                            </Link>
                        </div>
                    </div>
                </div>
            </section>

            {/* Features */}
            <section className="py-32 bg-white w-full px-6">
                <div className="max-w-7xl mx-auto grid md:grid-cols-3 gap-16">
                    <div className="space-y-6">
                        <div className="w-16 h-16 bg-cyan-50 rounded-3xl flex items-center justify-center">
                            <Check className="w-8 h-8 text-cyan-600" />
                        </div>
                        <h3 className="text-3xl font-black tracking-tight">Salt-Air Specialized</h3>
                        <p className="text-cyan-900/60 leading-relaxed font-medium text-lg">We use specialized eco-friendly solutions to cut through St Kilda's coastal salt spray and grime.</p>
                    </div>
                    <div className="space-y-6">
                        <div className="w-16 h-16 bg-cyan-50 rounded-3xl flex items-center justify-center">
                            <Star className="w-8 h-8 text-cyan-600" />
                        </div>
                        <h3 className="text-3xl font-black tracking-tight">Luxury Care</h3>
                        <p className="text-cyan-900/60 leading-relaxed font-medium text-lg">Meticulous cleaning of sills, frames, and tracks. We leave your home cleaner than we found it.</p>
                    </div>
                    <div className="space-y-6">
                        <div className="w-16 h-16 bg-cyan-50 rounded-3xl flex items-center justify-center">
                            <MapPin className="w-8 h-8 text-cyan-600" />
                        </div>
                        <h3 className="text-3xl font-black tracking-tight">Pure 3182 Local</h3>
                        <p className="text-cyan-900/60 leading-relaxed font-medium text-lg">Serving St Kilda, St Kilda East, and Elwood with prompt, professional service every day.</p>
                    </div>
                </div>
            </section>

            {/* Quote Form Overlay */}
            <section id="quote" className="py-32 bg-cyan-950 w-full text-white relative">
                <div className="absolute inset-0 opacity-10 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')]" />
                <div className="max-w-4xl mx-auto px-6 relative z-10 text-center">
                    <h2 className="text-4xl md:text-7xl font-black mb-12 tracking-tight">Clearer skies await.</h2>
                    <div className="bg-white/5 backdrop-blur-xl p-12 rounded-[48px] border border-white/10 shadow-2xl text-left">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div className="space-y-2">
                                <label className="text-xs font-black uppercase tracking-widest text-cyan-400">FullName</label>
                                <input type="text" className="w-full bg-white/10 border border-white/20 rounded-xl p-4 text-white outline-none focus:border-cyan-500 transition-colors" />
                            </div>
                            <div className="space-y-2">
                                <label className="text-xs font-black uppercase tracking-widest text-cyan-400">Email Address</label>
                                <input type="email" className="w-full bg-white/10 border border-white/20 rounded-xl p-4 text-white outline-none focus:border-cyan-500 transition-colors" />
                            </div>
                            <div className="space-y-2 md:col-span-2">
                                <label className="text-xs font-black uppercase tracking-widest text-cyan-400">Property Details (St Kilda Location)</label>
                                <textarea className="w-full bg-white/10 border border-white/20 rounded-xl p-4 text-white outline-none focus:border-cyan-500 transition-colors h-32"></textarea>
                            </div>
                            <button className="md:col-span-2 bg-cyan-500 py-6 rounded-2xl font-black text-xl hover:bg-cyan-600 transition-all shadow-xl shadow-cyan-900/50">Send Inquiry</button>
                        </div>
                    </div>
                </div>
            </section>

            {/* Footer */}
            <footer className="w-full py-16 bg-white px-6 border-t border-cyan-50">
                <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-8">
                    <div className="font-black text-cyan-900 text-sm tracking-[0.3em] uppercase underline decoration-cyan-500 decoration-4 underline-offset-8">ST KILDA GLASS CO.</div>
                    <div className="text-cyan-900/30 font-bold text-xs tracking-widest uppercase">Expert Window Cleaning • Area 3182 • © 2026</div>
                </div>
            </footer>
        </main>
    );
}
